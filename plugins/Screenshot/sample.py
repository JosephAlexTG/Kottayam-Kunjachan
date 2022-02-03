@ScreenShotBot.on_callback_query(
    filters.create(lambda _, __, query: query.data.startswith("smpl"))
)
async def _(c, m):
    # c.process_pool.new_task(Utilities().sample_fn(c, m))
    try:
        await m.answer()
    except Exception:
        pass

    await m.edit_message_text(
        ms.ADDED_TO_QUEUE.format(per_user_process_count=Config.MAX_PROCESSES_PER_USER),
    )
    c.process_pool.new_task(
        (
            m.from_user.id,
            ProcessFactory(
                process_type=ProcessTypes.SAMPLE_VIDEO, client=c, input_message=m
            ),
        )
    )
